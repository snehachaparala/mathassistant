from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
#from PIL import Image as PILImage
import math
import sys
import time
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyautogui
import subprocess

# Create an MCP server
mcp = FastMCP("Calculator")

# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"

@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
    print("CALLED: review_code(code: str) -> str:")


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

@mcp.tool()
def reverse_string(text: str) -> str:
    """Reverse a string"""
    print("CALLED: reverse_string(text: str) -> str:")
    return text[::-1]

#@mcp.tool()
#def open_notes() -> str:
#    """Open the notes directory"""
#    print("CALLED: open_notes() -> str:")
#    notes_dir = os.path.expanduser("~/Notes")
#    if not os.path.exists(notes_dir):
#        os.makedirs(notes_dir)
#    os.system(f"open {notes_dir}")
#    return f"Opened notes directory at {notes_dir}"

#@mcp.tool()
#def create_note() -> str:
#    """Create a new note with current timestamp"""
#    print("CALLED: create_note() -> str:")
#    notes_dir = os.path.expanduser("~/Notes")
#    if not os.path.exists(notes_dir):
#        os.makedirs(notes_dir)
#    
#    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#    note_name = f"result_{timestamp}.txt"
#    note_path = os.path.join(notes_dir, note_name)
#    
#    with open(note_path, "w") as f:
#        f.write(f"Created at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
#    
#    os.system(f"open {note_path}")
#    return f"Created and opened note: {note_name}"

#@mcp.tool()
#def open_note(note_name: str) -> str:
#    """Open a specific note by name"""
#    print("CALLED: open_note(note_name: str) -> str:")
#    notes_dir = os.path.expanduser("~/Notes")
#    note_path = os.path.join(notes_dir, note_name)
#    
#    if not os.path.exists(note_path):
#        return f"Error: Note '{note_name}' not found"
#    
#    os.system(f"open {note_path}")
#    return f"Opened note: {note_name}"

#@mcp.tool()
#def create_note_with_content(content: str) -> str:
#    """Create a new note with the specified content"""
#    print("CALLED: create_note_with_content(content: str) -> str:")
#    notes_dir = os.path.expanduser("~/Notes")
#    if not os.path.exists(notes_dir):
#        os.makedirs(notes_dir)
#    
#    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#    note_name = f"result_{timestamp}.txt"
#    note_path = os.path.join(notes_dir, note_name)
#    
#    with open(note_path, "w") as f:
#        f.write(f"Created at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
#        f.write("-" * 50 + "\n")
#        f.write(content + "\n")
#    
#    os.system(f"open {note_path}")
#    return f"Created and opened note: {note_name}"

@mcp.tool()
def send_email(to_email: str, subject: str, body: str) -> str:
    """Send an email via Gmail SMTP.
    
    Args:
        to_email: Recipient email address
        subject: Email subject
        body: Email body content
    
    Returns:
        str: Success or error message
    """
    print("CALLED: send_email(to_email: str, subject: str, body: str) -> str:")
    
    from_email = ""
    app_password = ""
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Add body to email
        msg.attach(MIMEText(body, 'plain'))
        
        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login to the server
        server.login(from_email, app_password)
        
        # Send email
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        
        return f"Email sent successfully to {to_email}"
        
    except Exception as e:
        return f"Error sending email: {str(e)}"

@mcp.tool()
def automate_keynote(text: str) -> str:
    """Automate Keynote drawing activity:
    1. Opens Keynote application
    2. Creates a new presentation using Command + N
    3. Waits 5 seconds for the presentation to load
    4. Presses Enter to start with a blank slide
    5. Opens keyboard shortcuts (Shift + Command + K) to access drawing tools
    6. Types the provided text
    
    Args:
        text: The text to be typed at the end of the automation sequence
    
    Returns:
        str: Success or error message
    """
    #print("CALLED: automate_keynote(text: str) -> str:")
    
    try:
        # Open Keynote
        time.sleep(3)
        subprocess.Popen(['open', '-a', 'Keynote'])
        time.sleep(4)  # Wait for Keynote to open
        pyautogui.press('enter')
        # Create new presentation (Cmd + N)
        pyautogui.hotkey('command', 'n')
        time.sleep(5)  # Wait 5 seconds
        pyautogui.press('enter')
        time.sleep(8)
        # Open keyboard shortcuts (Shift + Cmd + K)
        pyautogui.hotkey('shift', 'command', 'k')
        time.sleep(4)
        pyautogui.press('enter')
        # Type the provided text
        pyautogui.write(text)

        time.sleep(2)
        return f"Successfully completed Keynote automation sequence and typed: {text}"
        
    except Exception as e:
        return f"Error during Keynote automation: {str(e)}"

# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        # Run with specific host and port for development
        mcp.run(host="127.0.0.1", port=8000)
    else:
        # Run with stdio for direct execution
        mcp.run(transport="stdio")