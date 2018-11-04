<template>
    <div class="columns is-centered">
        <div class="hero-body">
            <div class="container has-text-centered">
                <div class="column is-4 is-offset-4">
                    <h3 class="title has-text-grey">Login</h3>
                    <div class="box">
                        <form>
                            <div class="field">
                                <div class="control">
                                    <input v-model="form.username" class="input" type="username" placeholder="Your Username"
                                        autofocus="">
                                </div>
                            </div>
                            <div class="field">
                                <div class="control">
                                    <input v-model="form.password" class="input" type="password" placeholder="Your Password">
                                </div>
                            </div>
                            <div class="field">
                                <b-checkbox class="is-info">Remember me</b-checkbox>
                            </div>
                            <button @click="submitForm" class="button is-block is-fullwidth is-primary">Login</button>
                        </form>
                    </div>
                    <p class="has-text-grey">
                        <a href="../">Sign Up</a> &nbsp;·&nbsp;
                        <a href="../">Forgot Password</a> &nbsp;·&nbsp;
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data: function () {
        return {
            form: {
                username: '',
                password: ''
            }
        }
    },
    methods: {
        resetForm: function () {
            var self = this // *this* will refer to Object.keys below`
            Object.keys(this.form).forEach(function (key, index) {
                self.form[key] = ''
            })
        },

        submitForm: function (event) {
            this.ajaxRequest = true
            event.preventDefault()
            let url = '/login'
            this.$http.post(url, JSON.stringify(this.form))
                .then(response => {
                    this.resetForm()
                    this.$snackbar.open('Login succeesful')
                }).catch((err) => {
                    console.log(err)
                    this.$snackbar.open({ message: 'Error occured !', type: 'is-warning' })
                })
        }
    }
}
</script>
