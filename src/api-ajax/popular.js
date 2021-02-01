import http from './http';

export default{
    async getPopular(){
        return http.get('api-flask/popular.json');
    }
} 