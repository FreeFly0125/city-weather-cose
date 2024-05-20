import type { MutationTree } from 'vuex';
import type { RootState } from './states';
import type { CityClimatInfo, WeekelyForecastInfo } from './types';

export const mutations: MutationTree<RootState> = {
    CREATE_LOCATION(state: RootState, cityClimateInfo: CityClimatInfo) {
        state.citiesState.push(cityClimateInfo);
    },

    DELETE_LOCAION(state: RootState, id: number) {
        state.citiesState = state.citiesState.filter((item) => item.id !== id);
    },

    FORECAST_CLIMATE(state: RootState, info: WeekelyForecastInfo) {
        state.forecastState = info;
    },
};
