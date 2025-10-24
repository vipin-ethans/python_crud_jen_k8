# Use official NGINX image
FROM nginx:alpine

# Copy your static HTML/CSS/JS files into NGINX's default web directory
COPY index.html /usr/share/nginx/html/index.html

# Optional: If you have CSS or JS files, copy them too
# COPY style.css /usr/share/nginx/html/style.css
# COPY script.js /usr/share/nginx/html/script.js

# Expose port (not strictly needed unless running standalone)
EXPOSE 80

