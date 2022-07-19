<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="nombre">Nombre</label>
                <input
                    type="text"
                    class="form-control"
                    id="nombre"
                    v-model="propietario.nombre"
                    v-validate="'required'"
                    name="nombre"
                    placeholder="Ingres su nombre"
                    :class="{'is-invalid': errors.has('propietario.nombre') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="apellido">Apellido</label>
                <input
                    type="text"
                    class="form-control"
                    id="nombre"
                    v-model="propietario.apellido"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingres su apellido"
                    :class="{'is-invalid': errors.has('propietario.apellido') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
                <label for="cedula">Cédula</label>
                <input
                    type="text"
                    class="form-control"
                    id="cedula"
                    v-model="propietario.cedula"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingres su cédula"
                    :class="{'is-invalid': errors.has('propietario.cedula') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid cedula.
                </div>
            </div>

            <div class="form-group">
                <label for="correo">Correo</label>
                <input
                    type="text"
                    class="form-control"
                    id="correo"
                    v-model="propietario.correo"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingres su correo"
                    :class="{'is-invalid': errors.has('propietario.correo') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid correo.
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            propietario: {
                nombre: '',
                apellido: '',
                correo: '',
                cedula: '',
            },
            submitted: false
        }
    },
    methods: {
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                console.log(this.correo)
                axios.post('http://127.0.0.1:8000/api/propietarios/',
                        this.propietario
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>
