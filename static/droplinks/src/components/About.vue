<template>
  <div class="columns is-centered">
    <div class="column is-half is-offset-one-fifth">
      <div class="shadow col-xs-2 mb-3">
        <div class="LI-profile-badge"  data-version="v1" data-size="large" data-locale="en_US"  data-type="vertical" data-theme="dark" data-vanity="karansthr"><a class="LI-simple-link" href='https://in.linkedin.com/in/karansthr?trk=profile-badge'>Karan Suthar</a></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'About',
  mounted () {
    let linkedinBedgeScript = document.createElement('script')
    linkedinBedgeScript.setAttribute('src', 'https://platform.linkedin.com/badges/js/profile.js')
    document.head.appendChild(linkedinBedgeScript)
  }
}
</script>

<style>
</style>
