import type { Meta, StoryObj } from '@storybook/react-vite'
import { BarChart } from './BarChart'

const meta = {
	title: 'Graphs/BarChart',
	component: BarChart,
} satisfies Meta<typeof BarChart>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
	args: {
		data: {
			labels: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль'],
			datasets: [
				{
					label: 'Зарплаты по месяцам',
					data: [65, 59, 80, 81, 56, 55, 40],
					backgroundColor: 'rgba(16, 155, 71, 0.3)',
					borderColor: '#109B47',
					borderWidth: 1.5,
				},
			],
		},
	},
}