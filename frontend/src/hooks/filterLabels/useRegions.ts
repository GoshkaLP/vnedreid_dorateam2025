import { useEffect, useState } from 'react'

type SpecializationsResponse = {
  region: string
}[]

export const useRegions = () => {
  const [data, setData] = useState<SpecializationsResponse>()
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('http://10.10.162.1:8080/api/vacancies/filters/regions')
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch count')
        return res.json()
      })
      .then((data) => setData(data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [])

  const regions = data ? data.map((item) => item.region) : []

  return { regions, loading }
}
