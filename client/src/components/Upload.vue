<template>
  <div class="container">
    <div class="row align-items-center">
      <div class="col-12 mx-auto">
        <div class="card">
          <div class="card-body">
            <vue-dropzone
              ref="myVueDropzone"
              id="dropzone"
              :options="dropzoneOptions"
              :useCustomSlot="true"
            >
              <div class="dropzone-custom-content">
                <h3 class="dropzone-custom-title">
                  Drag and drop (or click) to upload tournament data!
                </h3>
                <div class="subtitle">
                  accepts tournament data in csv files as found on
                  <a href="http://www.tennis-data.co.uk/" target="_blank">
                    tennis-data.co.uk
                  </a>
                </div>
              </div>
            </vue-dropzone>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios';
import vue2Dropzone from 'vue2-dropzone';
import 'vue2-dropzone/dist/vue2Dropzone.min.css';

export default {
  name: 'Upload',
  components: {
    vueDropzone: vue2Dropzone,
  },
  data() {
    return {
      error: '',
      status: '',
      dropzoneOptions: {
        // eslint-disable-next-line
        url: process.env.VUE_APP_API_URL + 'tournament',
        thumbnailWidth: 200,
        maxFiles: 10,
        maxFileSize: 0.1,
        paramName: 'tournament',
        addRemoveLinks: true,
        error(file, response) {
          this.defaultOptions.error(file, response.message);
        },
      },
    };
  },
};
</script>

<style scoped>
.upload-wrapper {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  border: 1px solid #E4E6E7;
  box-shadow: 0px 2px 5px rgba(0,0,0,0.4);
}
.upload-wrapper h4 {
  font-size: 22px;
  margin: 0;
  padding: 0;
  margin-bottom: 40px;
}
.dropbox {
  outline: 2px dashed grey; /* the dash box */
  outline-offset: -10px;
  background: lightcyan;
  color: dimgray;
  padding: 10px 10px;
  min-height: 200px; /* minimum height */
  position: relative;
  cursor: pointer;
}
.input-file {
  opacity: 0; /* invisible but it's there! */
  width: 100%;
  height: 200px;
  position: absolute;
  cursor: pointer;
}
.dropbox:hover {
  background: lightblue; /* when mouse over to the drop zone, change color */
}
.dropbox p {
  font-size: 1.2em;
  text-align: center;
  padding: 50px 0;
}
</style>
