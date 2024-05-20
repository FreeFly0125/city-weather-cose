export interface CityClimatInfo {
    id: number;
    name: string;
    weather_code: number;
    temperature: number;
    rainfall: number;
}

export interface DailyForecastInfo {
    date: string;
    day: string;
    weather_code: number;
    min_temperature: number;
    max_temperature: number;
}

export interface WeekelyForecastInfo {
    name: string;
    country: string;
    forecast_info: DailyForecastInfo[];
}
