import axios from 'axios';

const API_URL = 'https://pw-sistema-de-teleconsultas.onrender.com/api/pacientes/';

// Configuração básica do Axios para incluir o token automaticamente
const getAuthHeader = () => {
  const token = localStorage.getItem('access_token');
  return token ? { Authorization: `Bearer ${token}` } : {};
};

export const pacienteService = {
  /**
   * Busca os dados do paciente logado atualmente (RN25/RN26)
   */
  async getMe() {
    try {
      const response = await axios.get(`${API_URL}me/`, {
        headers: getAuthHeader()
      });
      return response.data;
    } catch (error) {
      console.error("Erro ao buscar perfil do paciente:", error);
      throw error;
    }
  },

  /**
   * Atualiza os dados cadastrais do paciente
   * @param {Object} data - Objeto contendo os campos a serem alterados (PATCH)
   */
  async updateProfile(data) {
    try {
      const response = await axios.patch(`${API_URL}me/`, data, {
        headers: getAuthHeader()
      });
      return response.data;
    } catch (error) {
      console.error("Erro ao atualizar perfil:", error);
      throw error;
    }
  },

};