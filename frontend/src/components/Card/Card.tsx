import type { FC, ReactNode } from 'react'

import styles from './Card.module.css'
import classNames from 'classnames'

interface CardProps {
  className?: string,
  children: ReactNode
}

export const Card: FC<CardProps> = ({ className, children }) => {
	return (
		<div className={classNames(styles.root, className)}>
      {children}
    </div>
	)
}
