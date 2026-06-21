<template>
  <div class="login-wrapper d-flex justify-content-center align-items-center min-vh-100 py-5">
    <div class="login-card mx-3">
      
      <div class="text-center mb-4">
        <div class="logo-icon mx-auto mb-3 d-flex align-items-center justify-content-center">
          <i class="bi bi-stethoscope fs-3 text-white">T</i>
        </div>
        <h2 class="title fw-bold mb-1">MedConnect</h2>
        <p class="subtitle text-muted">Preencha os dados para se cadastrar como paciente</p>
      </div>

      <div class="toggle-container d-flex mb-4">
        <router-link to="/login" class="toggle-btn flex-fill text-center text-decoration-none">
          Entrar
        </router-link>
        <router-link to="/cadastro" class="toggle-btn flex-fill text-center text-decoration-none active">
          Cadastrar
        </router-link>
      </div>

      <div v-if="sucesso" class="alert alert-success py-2 px-3 small mb-3 rounded-3 d-flex align-items-center gap-2 alert-animated">
        <i class="bi bi-check-circle-fill fs-5 success-icon-pulse"></i>
        <div>
          <strong class="d-block">Cadastro realizado!</strong>
          <span class="text-secondary">Bem-vindo(a), {{ primeiroNome }}. Redirecionando...</span>
        </div>
      </div>

      <form @submit.prevent="handleRegister">
        <div class="mb-3">
          <label class="form-label">Nome Completo</label>
          <div class="input-wrapper position-relative">
            <i class="bi bi-person position-absolute icon-left"></i>
            <input 
              v-model="formData.nomeCompleto"
              type="text" 
              class="form-control custom-input" 
              placeholder="Seu nome completo" 
              :disabled="loading || sucesso"
              required
            />
          </div>
        </div>

        <div class="mb-3">
          <label class="form-label">CPF</label>
          <div class="input-wrapper position-relative">
            <i class="bi bi-card-text position-absolute icon-left"></i>
            <input 
              v-model="formData.cpf"
              type="text" 
              class="form-control custom-input" 
              placeholder="000.000.000-00" 
              :disabled="loading || sucesso"
              required
            />
          </div>
        </div>

        <div class="mb-3">
          <label class="form-label">E-mail</label>
          <div class="input-wrapper position-relative">
            <i class="bi bi-envelope position-absolute icon-left"></i>
            <input 
              v-model="formData.email"
              type="email" 
              class="form-control custom-input" 
              placeholder="seu@email.com" 
              :disabled="loading || sucesso"
              required
            />
          </div>
        </div>

        <div class="mb-3">
          <label class="form-label">Senha</label>
          <div class="input-wrapper position-relative">
            <i class="bi bi-lock position-absolute icon-left"></i>
            <input 
              v-model="formData.password"
              :type="showPassword ? 'text' : 'password'" 
              class="form-control custom-input pe-5" 
              placeholder="Sua senha" 
              :disabled="loading || sucesso"
              required
            />
            <i 
              class="bi position-absolute icon-right cursor-pointer" 
              :class="showPassword ? 'bi-eye' : 'bi-eye-slash'" 
              @click="!loading && !sucesso && (showPassword = !showPassword)">
            </i>
          </div>
        </div>

        <div class="mb-4">
          <label class="form-label">Confirmar senha</label>
          <div class="input-wrapper position-relative">
            <i class="bi bi-lock position-absolute icon-left"></i>
            <input 
              v-model="confirmPassword"
              :type="showPassword ? 'text' : 'password'" 
              class="form-control custom-input" 
              placeholder="Confirme sua senha" 
              :disabled="loading || sucesso"
              required
            />
          </div>
        </div>

        <button type="submit" class="btn btn-primary-custom w-100 py-2 mb-4 rounded-3 d-flex align-items-center justify-content-center gap-2" :disabled="loading || sucesso">
          <span v-if="loading" class="spinner-border spinner-border-sm" role="status"></span>
          <i v-else class="bi bi-person-plus"></i>
          {{ loading ? 'Criando conta...' : sucesso ? 'Redirecionando...' : 'Criar conta' }}
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
        Já tem uma conta?
        <router-link to="/login" class="brand-link text-decoration-none ms-1">Entrar</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const showPassword = ref(false)
const loading = ref(false)
const sucesso = ref(false)
const primeiroNome = ref('')
const confirmPassword = ref('')

const formData = reactive({
  nomeCompleto: '',
  email: '',
  password: '',
  cpf: '',
})

const handleRegister = async () => {
  if (formData.password !== confirmPassword.value) {
    alert('As senhas não coincidem!')
    return
  }

  loading.value = true
  sucesso.value = false

  try {
    const response = await axios.post('http://localhost:8000/api/pacientes/', formData)

    if (response.status === 201) {
      // Extrai apenas o primeiro nome para a mensagem elegante
      primeiroNome.value = formData.nomeCompleto.trim().split(' ')[0]
      sucesso.value = true
      loading.value = false

      // Redireciona após 1.5 segundos para visualização do feedback
      setTimeout(() => {
        router.push('/login')
      }, 1500)
    }
  } catch (error) {
    loading.value = false
    const serverErrors = error.response?.data
    let message = 'Erro ao realizar cadastro.'
    
    if (serverErrors) {
      message = Object.entries(serverErrors)
        .map(([key, value]) => `${key}: ${value}`)
        .join('\n')
    }
    
    alert(message)
    console.error('Erro detalhado:', serverErrors)
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
  max-width: 410px; /* Reduzido para um visual mais elegante e compacto */
  background: white; 
  border-radius: 20px; 
  box-shadow: 0 15px 35px rgba(4, 104, 191, 0.08); 
  padding: 1.75rem; /* Padding ideal para mobile */
}

/* Media query para telas médias/grandes (Tablets e Desktops) */
@media (min-width: 576px) {
  .login-card {
    padding: 2.5rem; /* Respiro interno ampliado apenas em telas maiores */
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
}
.custom-input:focus { 
  border-color: #0468BF; 
  box-shadow: 0 0 0 3px rgba(4, 104, 191, 0.1); 
  outline: none; 
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
.btn-social:hover { 
  background-color: #f8fafc; 
  border-color: #cbd5e1; 
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

/* Adicione isso no fim do <style scoped> do segundo arquivo */
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

.custom-input:disabled {
  background-color: #f8fafc;
  cursor: not-allowed;
}

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