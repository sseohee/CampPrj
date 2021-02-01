import axios from 'axios';

let baseUrl = '';

class Http {
  static parseUrl(url) { //별도 api서버 연결할 경우 해당주소로 변경해줌
    return `${baseUrl}/${url}`;
  }

  static get(url, data = null, config = {}) {
    if (data !== null) {
      config['params'] = data;
    }

    return axios.get(this.parseUrl(url), config).catch(error => {
      return Promise.reject(error.response);
    });
  }

  static post(url, data, config = null) {
    return axios.post(this.parseUrl(url), data, config).catch(error => {
      return Promise.reject(error.response);
    });
  }

  //flask 에 맞게 '_method' 수정

  static update(url, data = {}, config = null) {
    data['_method'] = 'put';

    return axios.post(this.parseUrl(url), data, config).catch(error => {
      return Promise.reject(error.response);
    });
  }
   //넘겨받은 데이터 ajax로 호출하는 기능
  static destroy(url, data = {}, config = null) {
    data['_method'] = 'delete';

    return axios.post(this.parseUrl(url), data, config).catch(error => {
      return Promise.reject(error.response);
    });
  }
}

export default Http;