<template>
    <div class="columns is-centered">
        <div class="hero-body">
            <div class="container has-text-centered">
                <div class="column is-4 is-offset-4">
                    <h3 class="title has-text-grey">Sign up</h3>
                    <div class="box">
                        <form>
                            <div class="field">
                                <div class="control">
                                    <input v-model="form.username" class="input" placeholder="username" autofocus="">
                                </div>
                            </div>
                            <div class="field">
                                <div class="control">
                                    <input v-model="form.email" class="input" type="email" placeholder="Your Email"
                                        autofocus="">
                                </div>
                            </div>
                            <div class="field">
                                <div class="control">
                                    <input v-model="form.password" class="input" type="password" placeholder="Your Password">
                                </div>
                            </div>
                            <div class="field">
                                <div class="control">
                                    <input v-model="form.repassword" class="input" type="password" placeholder="Re-enter Password">
                                </div>
                            </div>
                            <button @click="submitForm" class="button is-block is-primary is-fullwidth">Sign up</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Signup',
    data: function () {
        return {
            form: {
                username: '',
                email: '',
                password: '',
                repassword: ''
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
            let url = '/signup'
            this.$http.post(url, JSON.stringify(this.form))
                .then(response => {
                    this.resetForm()
                    this.$snackbar.open('Sign up succeesful')
                }).catch((err) => {
                    console.log(err)
                    this.$snackbar.open({ message: 'Error occured !', type: 'is-warning' })
                })
        }
    }
}
</script>
