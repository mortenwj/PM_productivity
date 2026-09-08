import type { ArgumentField, ArgumentValue, ComponentInstance } from '../types/components'
import { getCatalogEntry, getInstanceIndex, getInstanceLabel } from '../types/components'

interface ArgumentInspectorProps {
  instance: ComponentInstance
  allInstances: ComponentInstance[]
  onChange: (instanceId: string, key: string, value: ArgumentValue) => void
  onRemove: (instanceId: string) => void
}

function renderField(
  field: ArgumentField,
  value: ArgumentValue,
  onChange: (value: ArgumentValue) => void,
) {
  if (field.type === 'bool') {
    return (
      <label className="checkbox-row" key={field.key}>
        <input
          type="checkbox"
          checked={Boolean(value)}
          onChange={(e) => onChange(e.target.checked)}
        />
        {field.label}
      </label>
    )
  }

  if (field.type === 'text') {
    return (
      <div className="field field--full" key={field.key}>
        <label>{field.label}</label>
        <textarea
          rows={3}
          value={String(value ?? '')}
          onChange={(e) => onChange(e.target.value)}
        />
        {field.hint && <p className="hint">{field.hint}</p>}
      </div>
    )
  }

  if (field.type === 'number') {
    return (
      <div className="field" key={field.key}>
        <label>{field.label}</label>
        <input
          type="number"
          value={Number(value ?? field.defaultValue)}
          onChange={(e) => onChange(Number(e.target.value))}
        />
        {field.hint && <p className="hint">{field.hint}</p>}
      </div>
    )
  }

  return (
    <div className="field" key={field.key}>
      <label>{field.label}</label>
      <input
        type="text"
        value={String(value ?? '')}
        onChange={(e) => onChange(e.target.value)}
      />
      {field.hint && <p className="hint">{field.hint}</p>}
    </div>
  )
}

export function ArgumentInspector({ instance, allInstances, onChange, onRemove }: ArgumentInspectorProps) {
  const entry = getCatalogEntry(instance.kind)
  const index = instance.kind === 'DocumentReminder' ? 0 : getInstanceIndex(allInstances, instance.id)
  const title = getInstanceLabel(instance, index)

  return (
    <div className="argument-inspector">
      <div className="argument-inspector__header">
        <div>
          <h3 className="argument-inspector__title">{title}</h3>
          <p className="argument-inspector__meta">{entry.xamlType}</p>
        </div>
        <button
          type="button"
          className="btn btn--ghost btn--danger"
          onClick={() => onRemove(instance.id)}
        >
          Remove
        </button>
      </div>
      <p className="hint">{entry.description}</p>
      <div className="argument-inspector__fields">
        {entry.argumentFields.map((field) =>
          renderField(field, instance.arguments[field.key] ?? field.defaultValue, (value) =>
            onChange(instance.id, field.key, value),
          ),
        )}
      </div>
    </div>
  )
}
