<template>
    <div class="columns is-centered">
            <div class="hero-body">
                <div class="columns is-centered">
                    <div class="column is-6">
                        <h3 class="title has-text-grey">Contact me</h3>
                            <form
                                id="contact-form"
                                v-on:submit="submitForm"
                            >
                                <div class="field">
                                    <div class="control">
                                        <input v-model="form.name" class="input" type="text" placeholder="Your Name" autofocus="">
                                    </div>
                                </div>
                                <div class="field">
                                    <div class="control">
                                        <input v-model="form.email" class="input" type="email" placeholder="Your Email" autofocus="">
                                    </div>
                                </div>
                                <div class="field">
                                    <div class="control">
                                        <input v-model="form.subject" class="input" type="text" placeholder="Subject">
                                    </div>
                                </div>
                                <div class="field">
                                    <div class="control">
                                        <textarea v-model="form.message" class="textarea" placeholder="Hi..."></textarea>
                                    </div>
                                </div>
                                <button @click="submitForm" class="button is-block is-info is-large">Submit</button>
                            </form>
                        </div>
                </div>
            </div>
        </div>
</template>

<script>
/* eslint-disable */
export default{
  name: 'Contact',
  data: function() {
      return {
          form: {
            name: '',
            email: '',
            subject: '',
            message: ''
          }
      }
  },
  methods: {
    resetForm: function() {
        var self = this; //*this* will refer to Object.keys below`
        Object.keys(this.form).forEach(function(key,index) {
          self.form[key] = '';
        });
      },

    submitForm: function(event){
      this.ajaxRequest = true
      event.preventDefault()
      let url="/contact"
      this.$http.post(url, JSON.stringify(this.form))
      .then(response => {
      this.resetForm()
      this.$snackbar.open('You\'ll be hearing from me soon')
    }).catch((err) => {
      this.resetForm()
      console.log(err)
      this.$snackbar.open({message: 'Error occured !', type:'is-warning'})
      })
    }
  }
}
</script>
