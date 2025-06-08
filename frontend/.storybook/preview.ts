import type { Preview } from '@storybook/react-vite';
import '../src/fonts.css';

import Chart from 'chart.js/auto';
import annotationPlugin from 'chartjs-plugin-annotation';
import {
  BoxPlotController,
  BoxAndWiskers,
} from '@sgratzl/chartjs-chart-boxplot';

Chart.register(annotationPlugin);
Chart.register(BoxPlotController, BoxAndWiskers);

const preview: Preview = {
  parameters: {
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/i,
      },
    },
  },
};

export default preview;
