import { useEffect, useState } from 'react'

type ResumeCounterResponse = {
  count: number
}

export const useResumeCounter = ({query} : {query?: string}) => {
  const [data, setData] = useState<ResumeCounterResponse>()
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch(`http://10.10.162.1:8080/api/resume/count?${query}`)
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch count')
        return res.json()
      })
      .then((data) => setData(data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [query])

  const resumeCounter = {
    title: 'Всего соискателей',
    value: data?.count ?? 0,
  }

  return { resumeCounter, loading }
}
