# Use lightweight official Nginx Alpine image
FROM nginx:alpine

# Copy all project files into Nginx public directory
COPY . /usr/share/nginx/html

# Expose Nginx web server port
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
