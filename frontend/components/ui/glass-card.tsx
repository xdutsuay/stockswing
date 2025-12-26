import { cn } from "@/lib/utils";
import { HTMLAttributes, forwardRef } from "react";

interface GlassCardProps extends HTMLAttributes<HTMLDivElement> {
    variant?: "default" | "solid";
}

const GlassCard = forwardRef<HTMLDivElement, GlassCardProps>(
    ({ className, variant = "default", children, ...props }, ref) => {
        return (
            <div
                ref={ref}
                className={cn(
                    "rounded-2xl p-6 transition-all duration-300",
                    "glass-card border border-white/5",
                    "hover:border-white/10 hover:shadow-2xl hover:shadow-blue-500/10",
                    className
                )}
                {...props}
            >
                {children}
            </div>
        );
    }
);
GlassCard.displayName = "GlassCard";

export { GlassCard };
