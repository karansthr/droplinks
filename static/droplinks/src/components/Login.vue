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
                                        <input class="input" type="email" placeholder="Your Email" autofocus="">
                                    </div>
                                </div>
                                <div class="field">
                                    <div class="control">
                                        <input class="input" type="password" placeholder="Your Password">
                                    </div>
                                </div>
                                <div class="field">
                                    <b-checkbox class="is-info">Remember me</b-checkbox>
                                </div>
                                <button class="button is-block is-fullwidth is-primary">Login</button>
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
  name: 'Login'
}
</script>
