import type { CityClimatInfo, WeekelyForecastInfo } from './types';

export interface RootState {
    citiesState: CityClimatInfo[];
    forecastState: WeekelyForecastInfo;
    isShowSidebar: boolean;
}

export const state: RootState = {
    citiesState: [],
    forecastState: {
        name: '',
        country: '',
        forecast_info: [],
    },
    isShowSidebar: false,
};
