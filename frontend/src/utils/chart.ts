import Chart from 'chart.js/auto';
import annotationPlugin from 'chartjs-plugin-annotation';
import {
  BoxPlotController,
  BoxAndWiskers,
} from '@sgratzl/chartjs-chart-boxplot';

Chart.register(annotationPlugin);
Chart.register(BoxPlotController, BoxAndWiskers);
