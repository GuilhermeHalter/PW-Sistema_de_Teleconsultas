<template>
  <div class="login-wrapper d-flex justify-content-center align-items-center vh-100">
    <div class="login-card p-4 p-md-5">
      <h2 class="title fw-bold mb-2">Crie sua conta</h2>
      <p class="subtitle mb-4">Preencha os dados para se cadastrar como paciente</p>

      <div class="toggle-container d-flex mb-4">
        <router-link to="/login" class="toggle-btn flex-fill text-center text-decoration-none">
          Entrar
        </router-link>
        <router-link to="/cadastro" class="toggle-btn flex-fill text-center text-decoration-none active">
          Cadastrar
        </router-link>
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
              placeholder="........" 
              required
            />
            <i 
              class="bi position-absolute icon-right cursor-pointer" 
              :class="showPassword ? 'bi-eye' : 'bi-eye-slash'" 
              @click="showPassword = !showPassword">
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
              placeholder="........" 
              required
            />
          </div>
        </div>

        <button type="submit" class="btn btn-primary-custom w-100 py-2 mb-4" :disabled="loading">
          {{ loading ? 'Criando conta...' : 'Criar conta' }}
        </button>
      </form>

      <div class="divider d-flex align-items-center mb-4">
        <hr class="flex-grow-1" />
        <span class="mx-3 text-muted text-uppercase" style="font-size: 0.75rem;">OU</span>
        <hr class="flex-grow-1" />
      </div>

      <div class="row g-3 mb-4">
        <div class="col-6">
          <button class="btn btn-social w-100 d-flex align-items-center justify-content-center gap-2">
            <i class="bi bi-google text-dark"></i>
            <span class="text-dark">Google</span>
          </button>
        </div>
        <div class="col-6">
          <button class="btn btn-social w-100 d-flex align-items-center justify-content-center gap-2">
            <i class="bi bi-github text-dark"></i>
            <span class="text-dark">GitHub</span>
          </button>
        </div>
      </div>

      <p class="text-center mt-3 mb-0 text-muted" style="font-size: 0.9rem;">
        Já tem uma conta?
        <router-link to="/login" class="brand-link text-decoration-none">Entrar</router-link>
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
const confirmPassword = ref('')

// Dados organizados para bater com o Serializer do Django
const formData = reactive({
  nomeCompleto: '',
  email: '',
  password: '',
  cpf: '',
})

const handleRegister = async () => {
  // Validação de senha local
  if (formData.password !== confirmPassword.value) {
    alert('As senhas não coincidem!')
    return
  }

  loading.value = true

  try {
    // Chamada para o endpoint de pacientes
    const response = await axios.post('http://localhost:8000/api/pacientes/', formData)

    if (response.status === 201) {
      alert('Cadastro realizado com sucesso! Redirecionando para o login...')
      router.push('/login')
    }
  } catch (error) {
    // Captura erros de validação do Django (ex: E-mail ou CPF duplicados)
    const serverErrors = error.response?.data
    let message = 'Erro ao realizar cadastro.'
    
    if (serverErrors) {
      message = Object.entries(serverErrors)
        .map(([key, value]) => `${key}: ${value}`)
        .join('\n')
    }
    
    alert(message)
    console.error('Erro detalhado:', serverErrors)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* Mantive seus estilos originais com pequenos ajustes de usabilidade */
:root {
  --primary-color: #00A09D;
  --bg-toggle: #E6F3F3;
}

.login-wrapper {
  background-color: #FAFAFC;
}

.login-card {
  width: 100%;
  max-width: 480px;
}

.title {
  font-family: 'Merriweather', serif;
  color: #1A202C;
}

.toggle-container {
  background-color: #E6F3F3;
  border-radius: 8px;
  padding: 4px;
}

.toggle-btn {
  padding: 10px 0;
  border-radius: 6px;
  color: #4A5568;
  transition: 0.3s;
}

.toggle-btn.active {
  background-color: #fff;
  color: #1A202C;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.custom-input {
  padding-left: 2.6rem;
  border-radius: 8px;
}

.input-wrapper .icon-left {
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
}

.input-wrapper .icon-right {
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
}

.btn-primary-custom {
  background-color: #00A09D;
  border: none;
  border-radius: 8px;
  color: white;
}

.btn-primary-custom:disabled {
  background-color: #72c4c2;
}

.btn-social {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
}

.brand-link {
  color: #00A09D;
}

.cursor-pointer {
  cursor: pointer;
}
</style>