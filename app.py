import subprocess
import json
import re
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Whitelist of safe commands
ALLOWED_COMMANDS = {
    'ls': ['ls', 'ls -la', 'ls -l', 'ls -a'],
    'cd': ['cd'],
    'pwd': ['pwd'],
    'mkdir': ['mkdir'],
    'touch': ['touch'],
    'rm': ['rm', 'rm -r', 'rm -f'],
    'cp': ['cp'],
    'mv': ['mv'],
    'cat': ['cat'],
    'head': ['head'],
    'tail': ['tail'],
    'grep': ['grep'],
    'find': ['find'],
    'chmod': ['chmod'],
    'echo': ['echo'],
    'whoami': ['whoami'],
    'date': ['date'],
    'cal': ['cal'],
    'clear': ['clear'],
    'help': ['help'],
    'man': ['man'],
}

# Create sandbox directory
SANDBOX_DIR = '/tmp/bash_tutor_sandbox'
os.makedirs(SANDBOX_DIR, exist_ok=True)
os.chdir(SANDBOX_DIR)

def is_command_allowed(cmd):
    """Check if command is in whitelist"""
    cmd = cmd.strip()
    # Allow help command for any topic
    if cmd.startswith('help'):
        return True
    # Check if command starts with allowed base
    for base in ALLOWED_COMMANDS:
        if cmd.startswith(base + ' ') or cmd == base:
            return True
    return False

def sanitize_command(cmd):
    """Remove dangerous characters"""
    # Remove semicolons, pipes, redirects to other commands
    cmd = re.sub(r'[;&|$>`]', '', cmd)
    # Remove environment variable access
    cmd = re.sub(r'\$\{?[\w]+\}?', '', cmd)
    return cmd.strip()

@app.route('/execute', methods=['POST'])
def execute_command():
    data = request.json
    command = data.get('command', '')
    
    if not command:
        return jsonify({'output': 'No command provided', 'error': True})
    
    # Sanitize
    command = sanitize_command(command)
    
    # Check whitelist
    if not is_command_allowed(command):
        return jsonify({
            'output': f'Command "{command.split()[0]}" not allowed yet!\nTry: ls, cd, pwd, mkdir, touch, cat, grep, or help',
            'error': True,
            'hint': 'Start with basic commands like ls or pwd'
        })
    
    try:
        # Execute in sandbox
        result = subprocess.run(
            command,
            shell=True,
            cwd=SANDBOX_DIR,
            capture_output=True,
            text=True,
            timeout=5
        )
        
        output = result.stdout if result.stdout else result.stderr
        if not output:
            output = '(command executed successfully)'
            
        return jsonify({'output': output, 'error': False})
        
    except subprocess.TimeoutExpired:
        return jsonify({'output': 'Command timed out', 'error': True})
    except Exception as e:
        return jsonify({'output': str(e), 'error': True})

@app.route('/reset', methods=['POST'])
def reset_sandbox():
    """Reset the sandbox to initial state"""
    try:
        subprocess.run('rm -rf *', shell=True, cwd=SANDBOX_DIR)
        return jsonify({'success': True, 'message': 'Sandbox reset!'})
    except:
        return jsonify({'success': False})

@app.route('/ls-sandbox', methods=['GET'])
def list_sandbox():
    """List files in sandbox"""
    try:
        files = os.listdir(SANDBOX_DIR)
        return jsonify({'files': files})
    except:
        return jsonify({'files': []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
