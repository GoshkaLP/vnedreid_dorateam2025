import type { FC } from 'react'
import { Chart } from 'react-chartjs-2'
import type { ChartData, ChartOptions } from 'chart.js'

import styles from './Radar.module.css'

type RadarProps = {
	data: ChartData<'radar', number[], string>
}

export const Radar: FC<RadarProps> = ({ data }) => {
	const options: ChartOptions<'radar'> = {
		responsive: true,
		maintainAspectRatio: false,
		interaction: {
			mode: 'index',
			intersect: false
		},
		plugins: {
			tooltip: {
				mode: 'index',
				intersect: false,
				callbacks: {
					label: (context) => {
						const label = context.dataset.label || ''
						const value = context.formattedValue
						return `${label}: ${value}`
					},
				},
			},
			legend: {
				position: 'right',
				labels: {
					font: { size: 12 },
				},
			},
		},
		scales: {
			r: {
				beginAtZero: true,
				ticks: {
					maxTicksLimit: 10,
				},
				pointLabels: {
					font: {
						size: 12,
					},
				},
			},
		},
	}

	return (
		<div className={styles.root}>
			<Chart type='radar' data={data} options={options} />
		</div>
	)
}
