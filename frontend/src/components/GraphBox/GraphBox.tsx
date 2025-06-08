import type { FC, ReactNode } from 'react'

import styles from './GraphBox.module.css'

interface GraphBoxProps {
	title: ReactNode
	hint?: string
	onHintClick?: () => void
	children: ReactNode
}

export const GraphBox: FC<GraphBoxProps> = ({
	title,
	hint,
	onHintClick,
	children,
}) => {
	return (
		<div className={styles.root}>
			<div className={styles.header}>
				<h2 className={styles.title}>{title}</h2>

				{hint && (
					<button className={styles.hint} onClick={onHintClick}>
						{hint}
					</button>
				)}
			</div>

			{children}
		</div>
	)
}
