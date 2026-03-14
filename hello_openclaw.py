#!/usr/bin/env python3
"""
Hello OpenClaw - A friendly introduction to AI-powered automation
"""

import datetime
import json
from pathlib import Path


class OpenClawGreeting:
    """A simple class to demonstrate Python integration with OpenClaw"""
    
    def __init__(self, name="OpenClaw"):
        self.name = name
        self.created_at = datetime.datetime.now()
    
    def greet(self, user="World"):
        """Generate a personalized greeting"""
        return f"👋 Hello {user}! I'm {self.name}, your AI assistant."
    
    def status(self):
        """Return current status as a dictionary"""
        uptime = datetime.datetime.now() - self.created_at
        return {
            "name": self.name,
            "status": "online",
            "uptime_seconds": uptime.total_seconds(),
            "capabilities": [
                "file_management",
                "code_execution",
                "web_search",
                "task_automation",
                "natural_conversation"
            ]
        }
    
    def save_log(self, message, log_file="openclaw.log"):
        """Append a message to the log file"""
        timestamp = datetime.datetime.now().isoformat()
        log_path = Path(log_file)
        
        with log_path.open("a") as f:
            f.write(f"[{timestamp}] {message}\n")
        
        return f"Logged: {message}"


def main():
    """Main entry point"""
    assistant = OpenClawGreeting("OpenClaw Assistant")
    
    print(assistant.greet("alpiko"))
    print("\nCurrent Status:")
    print(json.dumps(assistant.status(), indent=2))
    
    # Log this interaction
    assistant.save_log("Hello OpenClaw example executed successfully")
    print("\n✅ Log entry created")


if __name__ == "__main__":
    main()
