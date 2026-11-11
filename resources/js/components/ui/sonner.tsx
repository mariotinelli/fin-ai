import type { CSSProperties } from "react"
import { Toaster as Sonner, type ToasterProps } from "sonner"

import { useAppearance } from "@/hooks/use-appearance"
import { useFlashToast } from "@/hooks/use-flash-toast"

function Toaster({ ...props }: ToasterProps) {
  const { appearance } = useAppearance()

  useFlashToast()

  return (
    <Sonner
      theme={appearance}
      className="toaster group"
      position="bottom-right"
      toastOptions={{
        classNames: {
          toast: "!shadow-overlay",
          success: "!border-positive !bg-positive !text-primary-foreground",
          error: "!border-destructive !bg-destructive !text-destructive-foreground",
        },
      }}
      style={
        {
          "--normal-bg": "var(--foreground)",
          "--normal-text": "var(--background)",
          "--normal-border": "var(--foreground)",
          "--border-radius": "var(--radius-control)",
          "--success-bg": "var(--positive)",
          "--success-text": "var(--primary-foreground)",
          "--success-border": "var(--positive)",
          "--error-bg": "var(--destructive)",
          "--error-text": "var(--destructive-foreground)",
          "--error-border": "var(--destructive)",
        } as CSSProperties
      }
      {...props}
    />
  )
}

export { Toaster }
