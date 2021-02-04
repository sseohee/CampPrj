import http from './http';

export default{
    async getMyloca(){
        return http.get('https://169.56.114.101:5000/main');
    }
} 