import type { ActionTree } from 'vuex';
import type { CityClimatInfo } from './types';
import type { RootState } from './states';
import axios from 'axios';

export const actions: ActionTree<RootState, RootState> = {
    async createLocation({ commit }, name: string) {
        try {
            const server_url = 'http://localhost:8000/locations';
            const body = { name: name };
            const newLocationRes = await axios.post<CityClimatInfo>(server_url, body);
            commit('CREATE_LOCATION', newLocationRes);
        } catch (e) {
            console.log(e);
        }
    },
    async deleteLocation({ commit }, id: number) {
        try {
            const server_url = 'http://localhost:8000/locations';
            const params = { id: id };
            await axios.delete<CityClimatInfo>(server_url, { params });
            commit('DELETE_LOCAION', id);
        } catch (e) {
            console.log(e);
        }
    },
    async forecastCityClimate({ commit }, id: number) {
        try {
            const server_url = 'http://localhost:8000/forecast';
        } catch (e) {}
    },
};
