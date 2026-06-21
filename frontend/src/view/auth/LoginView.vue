<template>
  <div class="login-wrapper d-flex justify-content-center align-items-center vh-100">
    <div class="login-card mx-3">      
      <div class="text-center mb-4">
        <div class="logo-icon mx-auto mb-3 d-flex align-items-center justify-content-center">
          <i class="bi bi-stethoscope fs-3 text-white">T</i>
        </div>
        <h2 class="title fw-bold mb-1">MedConnect</h2>
        <p class="subtitle text-muted">Entre com suas credenciais para acessar sua conta</p>
      </div>

      <div class="toggle-container d-flex mb-4">
        <router-link to="/login" class="toggle-btn flex-fill text-center text-decoration-none active">
          Entrar
        </router-link>
        <router-link to="/cadastro" class="toggle-btn flex-fill text-center text-decoration-none">
          Cadastrar
        </router-link>
      </div>

      <div v-if="erro" class="alert alert-danger py-2 px-3 small mb-3 rounded-3 d-flex align-items-center gap-2 alert-animated">
        <i class="bi bi-exclamation-triangle-fill fs-6"></i>
        <span>{{ erro }}</span>
      </div>

      <div v-if="sucesso" class="alert alert-success py-2 px-3 small mb-3 rounded-3 d-flex align-items-center gap-2 alert-animated">
        <i class="bi bi-check-circle-fill fs-5 success-icon-pulse"></i>
        <div>
          <strong class="d-block">Acesso permitido!</strong>
          <span class="text-secondary">Bem-vindo(a), {{ nomeUsuarioSucesso }}.</span>
        </div>
      </div>

      <form @submit.prevent="handleLogin">
        <div class="mb-3">
          <label class="form-label">E-mail</label>
          <div class="input-wrapper position-relative">
            <i class="bi bi-envelope position-absolute icon-left"></i>
            <input v-model="email" type="email" class="form-control custom-input" placeholder="seu@email.com" :disabled="loading || sucesso" required />
          </div>
        </div>

        <div class="mb-3">
          <label class="form-label">Senha</label>
          <div class="input-wrapper position-relative">
            <i class="bi bi-lock position-absolute icon-left"></i>
            <input v-model="password" :type="showPassword ? 'text' : 'password'" class="form-control custom-input pe-5" placeholder="Sua senha" :disabled="loading || sucesso" required />
            <i class="bi position-absolute icon-right cursor-pointer" :class="showPassword ? 'bi-eye' : 'bi-eye-slash'" @click="showPassword = !showPassword"></i>
          </div>
        </div>

        <div class="d-flex justify-content-between align-items-center mb-4 mt-2">
          <div class="form-check d-flex align-items-center">
            <input class="form-check-input custom-checkbox mt-0 me-2" type="checkbox" id="lembrar" v-model="rememberMe" :disabled="loading || sucesso" />
            <label class="form-check-label text-muted label-sm" for="lembrar">Lembrar de mim</label>
          </div>
          <a href="#" class="brand-link text-decoration-none small fw-semibold">Esqueceu a senha?</a>
        </div>

        <button type="submit" class="btn btn-primary-custom w-100 py-2 mb-4 rounded-3 d-flex align-items-center justify-content-center gap-2" :disabled="loading || sucesso">
          <span v-if="loading" class="spinner-border spinner-border-sm" role="status"></span>
          <i class="bi bi-box-arrow-in-right"></i>
          {{ loading ? 'Autenticando...' : sucesso ? 'Redirecionando...' : 'Entrar' }}
        </button>
      </form>

      <div class="divider d-flex align-items-center mb-4">
        <hr class="flex-grow-1" />
        <span class="mx-3 text-muted text-uppercase" style="font-size: 0.75rem; font-weight: 700; letter-spacing: 0.5px;">OU</span>
        <hr class="flex-grow-1" />
      </div>

      <div class="row g-3 mb-4">
        <div class="col-6">
          <button class="btn btn-social w-100 d-flex align-items-center justify-content-center gap-2 py-2" :disabled="loading || sucesso">
            <i class="bi bi-google text-dark"></i>
            <span class="text-dark small fw-semibold">Google</span>
          </button>
        </div>
        <div class="col-6">
          <button class="btn btn-social w-100 d-flex align-items-center justify-content-center gap-2 py-2" :disabled="loading || sucesso">
            <i class="bi bi-github text-dark"></i>
            <span class="text-dark small fw-semibold">GitHub</span>
          </button>
        </div>
      </div>

      <p class="text-center mt-3 mb-0 text-muted small">
        Não tem uma conta?
        <router-link to="/cadastro" class="brand-link text-decoration-none ms-1">Cadastre-se aqui</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const showPassword = ref(false)
const email = ref('')
const password = ref('')
const rememberMe = ref(false)
const loading = ref(false)
const erro = ref('')
const sucesso = ref(false)
const nomeUsuarioSucesso = ref('')

const handleLogin = async () => {
  loading.value = true
  erro.value = ''
  sucesso.value = false
  
  try {
    const baseUrl = axios.defaults.baseURL || 'https://pw-sistema-de-teleconsultas.onrender.com'
    
    // ETAPA 1: Autenticação para pegar os tokens de acesso
    const responseAuth = await axios.post(`${baseUrl}/api/token/`, {
      email: email.value, 
      password: password.value
    })

    const { access, refresh } = responseAuth.data
    localStorage.setItem('access_token', access)
    localStorage.setItem('refresh_token', refresh)

    if (rememberMe.value) {
      localStorage.setItem('remembered_email', email.value)
    } else {
      localStorage.removeItem('remembered_email')
    }

    // ETAPA 2: Buscar as informações do Usuário
    const responseUsuarios = await axios.get(`${baseUrl}/api/usuarios/`, {
      headers: {
        Authorization: `Bearer ${access}`
      }
    })

    console.log('Lista de usuários retornada da API:', responseUsuarios.data)

    let usuarioLogado = null
    if (Array.isArray(responseUsuarios.data)) {
      usuarioLogado = responseUsuarios.data.find(
        u => u.Email?.toLowerCase() === email.value.toLowerCase() || u.email?.toLowerCase() === email.value.toLowerCase()
      )
    } else if (responseUsuarios.data && typeof responseUsuarios.data === 'object') {
      usuarioLogado = responseUsuarios.data
    }

    if (!usuarioLogado) {
      throw new Error('Perfil de usuário correspondente não foi encontrado na listagem.')
    }

    const rawRole = usuarioLogado.Role || usuarioLogado.role || 'Paciente'
    const nomeCompleto = usuarioLogado.NomeCompleto || usuarioLogado.nomeCompleto || 'Usuário'

    const normalizarRole = rawRole.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toUpperCase().trim()

    localStorage.setItem('user_role', normalizarRole)
    localStorage.setItem('user_name', nomeCompleto)

    console.log('Usuário autenticado:', nomeCompleto, '| Role:', normalizarRole)

    // Ativa o estado de sucesso e guarda o nome para o card
    nomeUsuarioSucesso.value = nomeCompleto.split(' ')[0] // Pega apenas o primeiro nome para ficar elegante
    sucesso.value = true
    loading.value = false

    // ETAPA 3: Redirecionamento com delay para o usuário ver o feedback visual
    setTimeout(() => {
      if (normalizarRole === 'ADMIN' || normalizarRole === 'ADMINISTRADOR') {
        router.push({ name: 'admin-dashboard' })
      } else if (normalizarRole === 'MEDICO') {
        router.push({ name: 'dashboard-medico' })
      } else {
        router.push({ name: 'dashboard-paciente' })
      }
    }, 1500)

  } catch (error) {
    console.error('Erro no fluxo de autenticação:', error)
    loading.value = false
    if (error.response?.status === 401) {
      erro.value = 'E-mail ou senha inválidos.'
    } else {
      erro.value = error.message || 'Não foi possível conectar ao servidor backend.'
    }
  }
}
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

/* Wrapper principal */
.login-wrapper { 
  background: linear-gradient(135deg, #e0f2fe 0%, #dff2f0 100%); 
}

/* Card de Login Ajustado e Responsivo */
.login-card { 
  width: 100%; 
  max-width: 410px; 
  background: white; 
  border-radius: 20px; 
  box-shadow: 0 15px 35px rgba(4, 104, 191, 0.08); 
  padding: 1.75rem; 
}

@media (min-width: 576px) {
  .login-card {
    padding: 2.5rem; 
  }
}

/* Ícone do Logo */
.logo-icon { 
  width: 52px; 
  height: 52px; 
  background: linear-gradient(135deg, #0468BF, #03A1E0); 
  border-radius: 14px; 
}

/* Tipografia */
.title { 
  font-family: 'Merriweather', serif; 
  color: #1A202C; 
  font-size: 1.6rem;
}
.subtitle {
  font-size: 0.9rem;
}

/* Container de Alternância (Login/Cadastro) */
.toggle-container { 
  background-color: #E6F3F3; 
  border-radius: 10px; 
  padding: 4px; 
}
.toggle-btn { 
  padding: 8px 0; 
  border-radius: 8px; 
  color: #4A5568; 
  transition: 0.3s; 
  font-weight: 500; 
  font-size: 0.9rem;
}
.toggle-btn.active { 
  background-color: #fff; 
  color: #0468BF; 
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08); 
  font-weight: 600; 
}

/* Estilos customizados para os Alerts (Erro/Sucesso) */
.alert-animated {
  animation: fadeInDown 0.3s ease-out forwards;
}

.alert-success {
  background-color: #ecfdf5;
  border: 1px solid #a7f3d0;
  color: #065f46;
}

.success-icon-pulse {
  color: #10b981;
  animation: pulse 1.5s infinite ease-in-out;
}

/* Inputs e Formulários */
.form-label { 
  font-size: 0.85rem; 
  font-weight: 600; 
  color: #1e293b; 
}
.custom-input { 
  padding-left: 2.6rem; 
  border-radius: 10px; 
  border: 1.5px solid #e2e8f0; 
  padding-top: 10px; 
  padding-bottom: 10px; 
  font-size: 0.9rem; 
  color: #334155; 
  transition: all 0.2s;
}
.custom-input:focus { 
  border-color: #0468BF; 
  box-shadow: 0 0 0 3px rgba(4, 104, 191, 0.1); 
  outline: none; 
}
.custom-input:disabled {
  background-color: #f8fafc;
  cursor: not-allowed;
}

/* Posicionamento dos Ícones nos Inputs */
.input-wrapper .icon-left { 
  left: 14px; 
  top: 50%; 
  transform: translateY(-50%); 
  color: #94a3b8; 
  font-size: 1rem; 
}
.input-wrapper .icon-right { 
  right: 14px; 
  top: 50%; 
  transform: translateY(-50%); 
  color: #94a3b8; 
  font-size: 1rem; 
}

.label-sm { 
  font-size: 0.85rem; 
}
.custom-checkbox { 
  border-radius: 4px; 
  border: 1.5px solid #cbd5e1; 
}
.custom-checkbox:checked { 
  background-color: #0468BF; 
  border-color: #0468BF; 
}

/* Botões */
.btn-primary-custom { 
  background: linear-gradient(135deg, #0468BF, #03A1E0); 
  border: none; 
  color: white; 
  font-weight: 600; 
  font-size: 0.95rem; 
  transition: all 0.2s; 
}
.btn-primary-custom:hover:not(:disabled) { 
  opacity: 0.9; 
  transform: translateY(-1px); 
}
.btn-primary-custom:disabled { 
  opacity: 0.7; 
  cursor: not-allowed; 
}

.btn-social { 
  border: 1.5px solid #e2e8f0; 
  background-color: white; 
  border-radius: 10px; 
  transition: all 0.2s; 
}
.btn-social:hover:not(:disabled) { 
  background-color: #f8fafc; 
  border-color: #cbd5e1; 
}
.btn-social:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Divisores e Links */
.divider hr { 
  border-top: 1.5px solid #e2e8f0; 
  opacity: 1; 
}
.brand-link { 
  color: #0468BF; 
  font-weight: 600; 
}
.cursor-pointer { 
  cursor: pointer; 
}

/* Animações Keyframes */
@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.15); }
  100% { transform: scale(1); }
}
</style>