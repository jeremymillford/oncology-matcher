FROM node:16

WORKDIR /usr/src/app

# Copy dependencies
COPY package.json ./
RUN npm install

# Copy React app files
COPY src/ ./src
COPY public/ ./public

# Command to start React development server
CMD ["npm", "start"]
