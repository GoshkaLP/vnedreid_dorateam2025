import type { FC } from 'react'
import { Chart } from 'react-chartjs-2'
import type { ChartData } from 'chart.js'
import type { BoxPlotDataPoint } from '@sgratzl/chartjs-chart-boxplot'

import styles from './SampleGraph.module.css'

type SampleGraphProps = {
	data: ChartData<'boxplot', BoxPlotDataPoint[], string>
}

export const SampleGraph: FC<SampleGraphProps> = ({ data }) => {
	const options = {
		responsive: true,
		maintainAspectRatio: false,
		plugins: {
			legend: {
				position: 'top',
				labels: {
					font: { size: 12 },
				},
			},
			title: {
				display: true,
				text: 'Boxplot Chart',
				font: {
					size: 16,
				},
			},
			// annotation: {
			// 	annotations: {
			// 		targetLine: {
			// 			type: 'line',
			// 			yMin: 3.5,
			// 			yMax: 3.5,
			// 			borderColor: '#e74c3c',
			// 			borderWidth: 2,
			// 			borderDash: [6, 4],
			// 			label: {
			// 				display: true,
			// 				content: 'Целевая линия: 3.5',
			// 				color: '#007aff',
			// 				font: {
			// 					size: 12,
			// 					weight: 'bold',
			// 				},
			// 				backgroundColor: 'rgba(0, 122, 255, 0.1)',
			// 				position: 'start',
			// 				yAdjust: -10,
			// 				padding: 4,
			// 			},
			// 		},
			// 	},
			// },
		},
		scales: {
			y: {
				beginAtZero: true,
				ticks: {
					stepSize: 1,
				},
				title: {
					display: true,
					text: 'Значения',
				},
			},
			x: {
				title: {
					display: true,
					text: 'Категории',
				},
			},
		},
	} as any

	return (
		<div className={styles.root}>
			{data && <Chart key={JSON.stringify(data)} type='boxplot' data={data} options={options} />}
		</div>
	)
}
