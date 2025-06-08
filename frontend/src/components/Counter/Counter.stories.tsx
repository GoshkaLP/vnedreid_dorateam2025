import type { Meta, StoryObj } from '@storybook/react-vite'

import { Counter } from './Counter'

const meta = {
	title: 'Main/Counter',
	component: Counter,
  render: (args) => (
    <div style={{maxWidth: '360px'}}>
      <Counter {...args} />
    </div>
  )
} satisfies Meta<typeof Counter>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
	args: {
    title: 'Всего вакансий',
    value: 2451
  },
}
