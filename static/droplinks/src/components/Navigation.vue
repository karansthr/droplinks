<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="/">
          <img src="../assets/logo.png" width="100" height="4z8">
        </a>
        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <router-link class="navbar-item" v-for="routes in links"
          v-bind:key="routes.id"
          :to="`${routes.page}`">{{routes.text}}
          </router-link>
        </div>
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/signup/" class="button is-primary">
                <strong>Sign up</strong>
              </router-link>
              <router-link to="/login/" class="button is-light">
                Log in
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
</template>

<script>
export default {
  name: 'Navigation',
  data () {
    return {
      links: [
        {
          id: 0,
          text: 'Home',
          page: '/'
        },
        {
          id: 1,
          text: 'About',
          page: '/about'
        },
        {
          id: 2,
          text: 'Contact',
          page: '/contact'
        }
      ]
    }
  }
}
</script>
