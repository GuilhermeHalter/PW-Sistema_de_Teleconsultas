import axios from 'axios';

// DEFINA A URL DO SEU BACKEND DJANGO AQUI
const BACKEND_URL = 'https://pw-sistema-de-teleconsultas.onrender.com';

const http = axios.create({
  // Mudamos de '/api' relativo para a URL absoluta do seu Django
  baseURL: `${BACKEND_URL}/api`
});

http.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

http.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      const refresh = localStorage.getItem('refresh_token');
      if (refresh) {
        try {
          // Aqui usamos axios puro e apontamos diretamente para a rota global do Django
          const res = await axios.post(`${BACKEND_URL}/api/token/refresh/`, { refresh });
          localStorage.setItem('access_token', res.data.access);
          error.config.headers.Authorization = `Bearer ${res.data.access}`;
          
          // Re-executa a chamada que falhou usando o cliente configurado
          return http(error.config);
        } catch (refreshError) {
          console.error("Falha ao renovar o token:", refreshError);
          localStorage.clear();
          window.location.href = '/login';
        }
      } else {
        localStorage.clear();
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

export const medicoService = {
  getMe: () => http.get('/medicos/me/'),
  updateMe: (data) => http.patch('/medicos/me/', data),
  listar: () => http.get('/medicos/'),
  buscarPorId: (id) => http.get(`/medicos/${id}/`),
  criar: (data) => http.post('/medicos/', data),
  atualizar: (id, data) => http.patch(`/medicos/${id}/`, data),
  excluir: (id) => http.delete(`/medicos/${id}/`),
};

export const pacienteService = {
  getMe: () => http.get('/pacientes/me/'),
  updateMe: (data) => http.patch('/pacientes/me/', data),
  listar: () => http.get('/pacientes/'),
  buscarPorId: (id) => http.get(`/pacientes/${id}/`),
  atualizar: (id, data) => http.patch(`/pacientes/${id}/`, data),
  excluir: (id) => http.delete(`/pacientes/${id}/`),
};

export const horarioService = {
  listarMeus: () => http.get('/horarios/'),
  listar: (params) => http.get('/horarios/', { params }),
  listarDisponiveis: (medicoId) => http.get(`/horarios/disponiveis/?medico_id=${medicoId}`),
  criar: (data) => http.post('/horarios/', data),
  atualizar: (id, data) => http.patch(`/horarios/${id}/`, data),
  excluir: (id) => http.delete(`/horarios/${id}/`),
};

export const consultaService = {
  listar: () => http.get('/consultas/'),
  criar: (data) => http.post('/consultas/', data),
  confirmarPagamento: (id) => http.post(`/consultas/${id}/confirmar_pagamento/`),
  cancelar: (id) => http.post(`/consultas/${id}/cancelar/`),
  finalizar: (id) => http.post(`/consultas/${id}/finalizar/`),
  buscarPorId: (id) => http.get(`/consultas/${id}/`),
  atualizar: (id, data) => http.patch(`/consultas/${id}/`, data),
  excluir: (id) => http.delete(`/consultas/${id}/`),
};

export const especialidadeService = {
  listar: () => http.get('/especialidades/'),
};

export default http;