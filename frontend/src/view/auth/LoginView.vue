<template>
  <div class="login-wrapper d-flex justify-content-center align-items-center vh-100">
    <div class="login-card p-4 p-md-5">
      <h2 class="title fw-bold mb-2">Bem-vindo de volta!</h2>
      <p class="subtitle mb-4">Entre com suas credenciais para acessar sua conta</p>

      <div class="toggle-container d-flex mb-4">
        <router-link 
          to="/login" 
          class="toggle-btn flex-fill text-center text-decoration-none active"
        >
          Entrar
        </router-link>

        <router-link 
          to="/cadastro" 
          class="toggle-btn flex-fill text-center text-decoration-none"
        >
          Cadastrar
        </router-link>
      </div>

      <form @submit.prevent="handleLogin">
        <div class="mb-3">
          <label class="form-label">E-mail</label>
          <div class="input-wrapper position-relative">
            <i class="bi bi-envelope position-absolute icon-left"></i>
            <input 
              v-model="email"
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
              v-model="password"
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

        <div class="d-flex justify-content-between align-items-center mb-4 mt-2">
          <div class="form-check d-flex align-items-center">
            <input class="form-check-input custom-checkbox mt-0 me-2" type="checkbox" id="lembrar" v-model="rememberMe" />
            <label class="form-check-label text-muted" for="lembrar" style="font-size: 0.9rem;">
              Lembrar de mim
            </label>
          </div>

          <a href="#" class="brand-link text-decoration-none" style="font-size: 0.9rem;">
            Esqueceu a senha?
          </a>
        </div>

        <button 
          type="submit" 
          class="btn btn-primary-custom w-100 py-2 mb-4"
          :disabled="loading"
        >
          {{ loading ? 'Autenticando...' : 'Entrar' }}
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
        Não tem uma conta?
        <router-link to="/cadastro" class="brand-link text-decoration-none">
          Cadastre-se
        </router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()

// Estados Reativos
const showPassword = ref(false)
const email = ref('')
const password = ref('')
const rememberMe = ref(false)
const loading = ref(false)

const handleLogin = async () => {
  loading.value = true
  
  try {
    // Chamada para o endpoint do SimpleJWT no Django
    const response = await axios.post('http://localhost:8000/api/token/', {
      email: email.value,
      password: password.value
    })

    // Sucesso: Armazenamos os tokens
    const { access, refresh } = response.data
    localStorage.setItem('access_token', access)
    localStorage.setItem('refresh_token', refresh)

    // Opcional: Salvar e-mail se 'Lembrar de mim' estiver ativo
    if (rememberMe.value) {
      localStorage.setItem('remembered_email', email.value)
    }

    alert('Login realizado com sucesso!')
    
    // Redireciona para a página principal (ex: Dashboard)
    router.push('/dashboard-paciente')

  } catch (error) {
    console.error('Erro no login:', error)
    
    if (error.response?.status === 401) {
      alert('E-mail ou senha inválidos.')
    } else {
      alert('Erro ao conectar com o servidor. Verifique se o backend está rodando.')
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* Estilos mantidos conforme seu padrão visual */
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
  opacity: 0.7;
  cursor: not-allowed;
}

.brand-link {
  color: #00A09D;
}

.cursor-pointer {
  cursor: pointer;
}
</style>