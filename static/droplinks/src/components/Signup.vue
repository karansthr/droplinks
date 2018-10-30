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
                                        <input class="input" type="email" placeholder="Your Email" autofocus="">
                                    </div>
                                </div>
                                <div class="field">
                                    <div class="control">
                                        <input class="input" type="password" placeholder="Your Password">
                                    </div>
                                </div>
                                <div class="field">
                                        <div class="control">
                                            <input class="input" type="password" placeholder="Re-enter Password">
                                        </div>
                                </div>
                                <button class="button is-block is-primary is-fullwidth">Sign up</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
</template>

<script>
export default {
  name: 'Signup'
}
</script>
