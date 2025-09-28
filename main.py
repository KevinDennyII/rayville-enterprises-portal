#!/usr/bin/env python3
"""
Main entry point for Rayville Enterprises Portal
Serves the static HTML site on port 5000
"""

import http.server
import socketserver
import os
import sys

def main():
    PORT = 5000
    
    # Ensure we're in the correct directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    class StaticFileHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            super().end_headers()
            
        def log_message(self, format, *args):
            # Simple logging
            print(f"[{self.address_string()}] {format % args}")
    
    try:
        with socketserver.TCPServer(("0.0.0.0", PORT), StaticFileHandler) as httpd:
            print(f"🚀 Rayville Enterprises Portal is running!")
            print(f"📍 Server: http://0.0.0.0:{PORT}")
            print(f"📁 Directory: {os.getcwd()}")
            print("✨ Your improved site features:")
            print("   • Sticky footer (CSS Grid layout)")
            print("   • Clean CSS organization (Josh Comeau methodology)")
            print("   • Modern design with backdrop blur effects")
            print("   • Responsive business cards")
            print("   • Professional typography")
            print("\n🌐 Access your site through the Replit preview panel!")
            print("Press Ctrl+C to stop the server\n")
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Server stopped gracefully.")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()