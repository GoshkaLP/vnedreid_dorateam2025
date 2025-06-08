import type { FC } from 'react'

import styles from './Counter.module.css'

interface CounterProps {
	title: string
  value: number
}

export const Counter: FC<CounterProps> = ({ title, value }) => {
	return (
		<div className={styles.root}>
      <p className={styles.title}>{title}</p>
      <div className={styles.divider} />
      <p className={styles.value}>{value}</p>
    </div>
	)
}
