<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="costo_departamento">Costo Departamento</label>
                <input
                    type="text"
                    class="form-control"
                    id="departamento"
                    v-model="departamento.costo_departamento"
                    v-validate="'required'"
                    name="costo_departamento"
                    placeholder="Ingrese costo departamento"
                    :class="{'is-invalid': errors.has('departamento.departamento') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="num_cuartos">Numero de cuartos</label>
                <input
                    type="text"
                    class="form-control"
                    id="cuartos"
                    v-model="departamento.num_cuartos"
                    v-validate="'required'"
                    name="num_cuartos"
                    placeholder="Ingrese numero de cuartos"
                    :class="{'is-invalid': errors.has('departamento.tipo') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
                <label for="num_banos">Numero banos</label>
                <input
                    type="text"
                    class="form-control"
                    id="banos"
                    v-model="departamento.num_banos"
                    v-validate="'required'"
                    name="num_banos"
                    placeholder="Ingrese numero de banos"
                    :class="{'is-invalid': errors.has('departamento.tipo') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
                <label for="valor">Valor Alicuota</label>
                <input
                    type="text"
                    class="form-control"
                    id="valor"
                    v-model="departamento.valor"
                    v-validate="'required'"
                    name="valor"
                    placeholder="Ingrese valor alicuota"
                    :class="{'is-invalid': errors.has('departamento.valor') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid valor.
                </div>
            </div>

            <div class="form-group">
              <br>
                <label for="propietario">Propietario</label>
                <select v-model="departamento.propietario">
                            <option v-for="e in propietariosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}</option>
                        </select>
            </div>
            <br>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamento: {
                departamento: '',
                tipo: '',
                propietario: '',
            },
            propietariosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getPropietariosList()
    },
    methods: {
      getPropietariosList() {
            axios
            .get('http://127.0.0.1:8000/api/propietarios/')
            .then(response => {
                this.propietariosList = response.data
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.post('http://127.0.0.1:8000/api/departamentos/',
                        this.departamento
                    )
                    .then(response => {
                        this.$router.push('/departamentos');
                    })
            });
        }
    },
}
</script>
