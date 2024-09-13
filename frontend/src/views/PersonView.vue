<template>
    <div class="container-fluid"> 
        <h2 class="alert mt-3">Django Rest-api and Vue</h2>

        <div class="row d-flex justify-content-center">
            <div class="col-xl-10 ">
                <h2 class="alert alert-secondary ">List of Persons</h2>
                <table class="table table-bordered table-striped table-hover mt-4 ">
                    <thead class="thead-dark">
                        <tr>
                            <th scope="col">Name</th>
                            <th scope="col">Family Name</th>
                            <th scope="col">Phone Number</th>
                            <th scope="col">Age</th>
                            <th scope="col">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="person in persons" :key="person.id">
                            <td>{{ person.name }}</td>
                            <td>{{ person.family_name }}</td>
                            <td>{{ person.phone_number }}</td>
                            <td>{{ person.age }}</td>
                            <td>
                                <button class="btn btn-outline-secondary" @click="editBtn(person.id)">Edit</button>
                                <button class="btn btn-outline-secondary" @click="deletePerson(person.id)">Delete</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="container-fluid m-3 d-flex justify-content-center">
                <div v-if="Object.keys(currentPerson).length !== 0">
                    <h2 class="alert alert-secondary">Edit Person Details</h2>
                    <form @submit.prevent="updatePerson(currentPerson.id)">
                        <div class="row">
                            <div class="col">
                                <div class="form-group">
                                    <label class="form-label float-left ml-2">Name</label>
                                    <input type="text" class="form-control" v-model="currentPerson.name">
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label class="form-label float-left ml-2">Family Name</label>
                                    <input type="text" class="form-control" v-model="currentPerson.family_name">
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <div class="form-group">
                                    <label class="form-label float-left ml-2">Phone Number</label>
                                    <input type="text" class="form-control" v-model="currentPerson.phone_number">
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label class="form-label float-left ml-2">Age</label>
                                    <input type="text" class="form-control" v-model="currentPerson.age">
                                </div>
                            </div>
                        </div>
                        <button type="submit" class="btn btn-success float-left ml-2">Update</button>
                    </form>
                </div>
                <div class="ml-3">
                    <h2 class="alert alert-secondary">Add A New Person</h2>
                    <form @submit.prevent="savePerson">
                        <div class="row">
                            <div class="col">
                                <div class="form-group">
                                    <label class="form-label float-left ml-2">Name</label>
                                    <input type="text" class="form-control" v-model="person.name">
                                </div>
                                <div class="form-group">
                                    <label class="form-label float-left ml-2">Family Name</label>
                                    <input type="text" class="form-control" v-model="person.family_name">
                                </div>
                                <div class="form-group">
                                    <label class="form-label float-left ml-2">Phone Number</label>
                                    <input type="text" class="form-control" v-model="person.phone_number">
                                </div>
                                <div class="form-group">
                                    <label class="form-label float-left ml-2">Age</label>
                                    <input type="text" class="form-control" v-model="person.age">
                                </div>
                            </div>
                        </div>
                        <button type="submit" class="btn btn-primary ml-2">Save</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            persons: [],
            currentPerson: {},
            api: 'http://127.0.0.1:8000/api',
            person: {
                name: '',
                family_name: '',
                phone_number: '',
                age: '',
            },
        };
    },
    mounted() {
        console.log('DOM is rendered');
    },
    created() {
        console.log('DOM is created');
        this.getPersons();
    },
    methods: {
        getPersons() {
            axios.get(`${this.api}/persons/`)
                .then(response => {
                    this.persons = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        savePerson() {
            axios.post(`${this.api}/persons/`, this.person, {
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            .then(response => {
                this.persons.push(response.data);
                this.person = { name: '', family_name: '', phone_number: '', age: '' };
            })
            .catch(error => {
                console.log(error);
            });
        },
        editBtn(id) {
            const person = this.persons.find(p => p.id === id);
            if (person) {
                this.currentPerson = { ...person };
            }
        },
        updatePerson(id) {
            axios.put(`${this.api}/persons/${id}/`, this.currentPerson, {
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            .then(response => {
                this.getPersons();
                this.currentPerson = {};
            })
            .catch(error => {
                console.log(error);
            });
        },
        deletePerson(id) {
            axios.delete(`${this.api}/persons/${id}/`)
                .then(response => {
                    this.getPersons();
                })
                .catch(error => {
                    console.log(error);
                });
        },
    },
};
</script>
