import http from './http';

export default{
    async getMyloca(){
        return http.get('https://169.56.114.101:5000/get_every_camping_locations');
    }
    ,

    async getCampingList(){
        return http.get('https://169.56.114.101:5000/get_every_camping_locations');
    }

} 