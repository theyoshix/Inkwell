import urllib.request
import urllib.error
import json
import re
import ast

def get_llm_suggestions(text, app_instance, theme="fantasy"):
    """
    The Modular Editor Spoke.
    Uses Inkwell's native urllib connection and Refined Vacuum parser.
    """
    system_prompt = (
        f"You are a professional copyeditor for a {theme} novel. "
        "Analyze the text for grammar, flow, and prose improvements. "
        "Respond ONLY with a valid JSON array. "
        'Format exactly like this: [{"message": "Reason for the change", "text": "The exact original word or phrase", "replacements": ["Suggested fix 1", "Suggested fix 2"]}]'
    )
    
    try:
        # Pull the connection settings from your main app UI
        mode = getattr(app_instance, 'ai_mode', 'local')
        api_key = getattr(app_instance, 'ai_api_key', '').strip()
        url_box = getattr(app_instance, 'ai_local_url', '').strip().rstrip('/')
        
        data = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Text: {text}"}
            ],
            "temperature": 0.2, 
            "max_tokens": 3000
        }
        
        if mode != 'local':
            data["model"] = "llama-3.3-70b-versatile"

        if mode == 'local':
            url = url_box if '/chat/completions' in url_box else url_box + '/v1/chat/completions'
        else:
            url = "https://api.groq.com/openai/v1/chat/completions" if ('groq' in url_box or not url_box) else url_box

        # Make the connection
        req = urllib.request.Request(url, method="POST")
        req.add_header('Content-Type', 'application/json')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        if mode != 'local' and api_key:
            req.add_header('Authorization', f"Bearer {api_key}")

        jsondata = json.dumps(data).encode('utf-8')
        
        with urllib.request.urlopen(req, data=jsondata, timeout=60) as response:
            raw_reply = json.loads(response.read().decode('utf-8'))['choices'][0]['message']['content'].strip()
            
            # --- THE REFINED VACUUM ---
            json_match = re.search(r'\[.*\]', raw_reply, re.DOTALL)
            
            if json_match:
                clean_string = json_match.group(0)
                try:
                    llm_suggestions = json.loads(clean_string)
                except json.JSONDecodeError:
                    try:
                        llm_suggestions = ast.literal_eval(clean_string)
                    except Exception as e:
                        return {"success": False, "error": f"JSON Parse Error: {str(e)}"}
            else:
                return {"success": True, "issues": []}

        # Format the data so your PyWebView Javascript can highlight it
        formatted_issues = []
        for item in llm_suggestions:
            orig_text = item.get("text", "")
            
            # Find the exact character offset in the main text
            start_idx = text.find(orig_text) 
            
            if start_idx != -1:
                formatted_issues.append({
                    'message': item.get("message", "Grammar/Lore Suggestion"),
                    'text': orig_text,
                    'start': start_idx,
                    'end': start_idx + len(orig_text),
                    'replacements': item.get("replacements", [])
                })
                
        return {"success": True, "issues": formatted_issues}
        
    except Exception as e:
        return {"success": False, "error": f"Lunaris API Error: {str(e)}"}