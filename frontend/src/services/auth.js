import axios from 'axios';

const api = axios.create({
  baseURL: '/api'
});

export const authService = {
  async login(email, password) {
    const response = await api.post('/token/', { email, password });
    if (response.data.access) {
      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);
    }
    return response.data;
  },

  async register(data) {
    const role = data.role || 'PACIENTE';
    const endpoint = role === 'MEDICO' ? '/medicos/' : '/pacientes/';
    const response = await api.post(endpoint, data);
    return response.data;
  },

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_role');
    localStorage.removeItem('user_name');
  },

  isAuthenticated() {
    return !!localStorage.getItem('access_token');
  },

  getRole() {
    return localStorage.getItem('user_role');
  }
};
