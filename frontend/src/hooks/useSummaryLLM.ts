import { useEffect, useState } from 'react'

type SummaryLLMResponse = {
  response: string
}

export const useSummaryLLM = ({query} : {query?: string}) => {
  const [data, setData] = useState<SummaryLLMResponse>()
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch(`http://10.10.162.1:8080/api/vacancies/summary_llm?${query}`)
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch summary_llm')
        return res.json()
      })
      .then((data) => setData(data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [query])

  const summaryLLM = {
    response: data?.response
  }

  return {
    summaryLLM,
    // summaryLLM:
    //   {
    //     response: '**Описание распределения:** Разрыв между **Q1 (72 402.5)** и **медианой (115 138.5)** значителен (**42 736**), указывая на большой разброс в нижней половине диапазона. Среднее значение (**115 051.29**) близко к медиане, а **Q3 (157 593)** значительно выше них. **Конкурентное предложение:** Для привлечения сильных кандидатов, предложение должно быть в верхнем квартиле. Рекомендованная вилка от **Q3 (157 593)** до **максимума (200 000)**, например **167 000**. *Выводы:* *Распределение ассиметрично с большим разбросом в нижней половине.* *Фокус на верхний квартиль создаст привлекательное и конкурентное предложение.*',
    //   },
    loading
  }
}
