import type { Meta, StoryObj } from '@storybook/react-vite'

import { Card } from './Card'

const meta = {
	title: 'Main/Card',
	component: Card,
} satisfies Meta<typeof Card>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
	args: {
    children: <p>{'some content'}</p>
  },
}
