@torch.jit.script
def quat_conjugate(q: torch.Tensor) -> torch.Tensor:
    return torch.cat((-q[..., 0:3], q[..., 3:4]), dim=-1)
