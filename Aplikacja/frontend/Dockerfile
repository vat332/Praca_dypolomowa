FROM node:16-alpine

WORKDIR /app
RUN npm install bootstrap@3
RUN npm install bulma
RUN npm install react-router-dom --save
RUN npm install react-token-auth
RUN npm install eslint-config-airbnb-base
RUN npm info "eslint-config-airbnb@latest" peerDependencies
RUN npm install -g install-peerdeps
RUN install-peerdeps --dev eslint-config-airbnb
RUN npm install eslint eslint-plugin-react --save-dev
RUN npm install
COPY package.json .
COPY . .

EXPOSE 3000
# required for docker desktop port mapping
CMD ["npm", "start", "dev"]
