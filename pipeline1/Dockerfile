# Use the latest Nginx image as the base image
FROM nginx:latest

# Set the working directory to the default Nginx HTML directory
WORKDIR /usr/share/nginx/html

# Copy the HTML, CSS, and other static files to the Nginx HTML directory
COPY . /usr/share/nginx/html/

# Expose port 80 to allow access to the web server
EXPOSE 80

# Command to start Nginx
CMD ["nginx", "-g", "daemon off;"]
