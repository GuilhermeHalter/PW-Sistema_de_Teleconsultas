import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api'
});

export const authService = {
  async login(email, password) {
    // Envia e-mail e senha para o endpoint que criamos acima
    const response = await api.post('/login/', { email, password });
    
    if (response.data.access) {
      // RN25: Salva o token no localStorage para manter a sessão
      localStorage.setItem('user_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);
    }
    return response.data;
  },

  logout() {
    localStorage.removeItem('user_token');
    localStorage.removeItem('refresh_token');
  }
};